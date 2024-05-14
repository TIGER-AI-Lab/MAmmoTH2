from openai import OpenAI
import datasets
import json
client = OpenAI()

def run_one_question(question: str):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an knowledge expert, you are supposed to answer the multi-choice question to derive your final answer as `The answer is ...`."
            },
            {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": question
                    }
                ]
            }
        ],
        temperature=0.1,
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content


def form_options(options: list):
    option_str = 'Options are:\n'
    opts = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for opt, o in zip(options, opts):
        option_str += f'({o}): {opt}' + '\n'
    return option_str


if __name__ == "__main__":
    dataset = datasets.load_dataset('TIGER-Lab/MMLU-Pro')

    categories = ['computer science', 'math', 'chemistry', 'engineering', 'law', 'biology',
                  'health', 'physics', 'business', 'philosophy', 'economics', 'other',
                  'psychology', 'history']

    prompts = {c: '' for c in categories}
    for d in dataset['validation']:
        prompts[d['category']] += 'Q:' + ' ' + d['question'] + '\n' + form_options(d['options']) + '\n' + d['cot_content'] + '\n\n'


    per_category_accuracy = {c: [0, 0] for c in categories}
    success, fail = 0, 0
    answers = []

    print('----------------- Start Answering -------------------')
    for entry in dataset['test']:
        print(entry)
        prefix = prompts[entry['category']]
        query = prefix + 'Q: ' + entry['question'] + '\n' + form_options(entry['options']) + '\n'
        answer = run_one_question(query)
        # print(answer)
        entry['solution'] = answer
        answers.append(entry)

        prediction = answer.split('The answer is ')[-1]
        if f'({entry["answer"]})'.lower() in prediction.lower():
            success += 1
            per_category_accuracy[entry['category']][0] += 1
        else:
            fail += 1
            per_category_accuracy[entry['category']][1] += 1

        print(success / (success + fail))

    with open('outputs.json', 'w') as f:
        json.dump(answers, f, indent=2)

    for k, v in per_category_accuracy.items():
        print('accuracy: ', k, v[0] / (v[0] + v[1]))
