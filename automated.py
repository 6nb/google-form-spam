from bs4 import BeautifulSoup
import requests
import re

def submit(url, data):
    res = requests.post(url, data)
    print(f'[{res.status_code}] {res.reason}')

def main():
    
    # Request and parse form
    view_url = input('Form link: ')
    view_form = requests.get(view_url)
    if not view_form.status_code == 200: raise Exception('Failed to get form.')
    form = BeautifulSoup(view_form.content, 'html.parser')
    title = form.find(class_="freebirdFormviewerViewHeaderTitle")
    print(f'Found form: "{"Untitled" if not title else title.text}"')

    # Prompt for each question, filling in data
    data = {}
    for index, item in enumerate(form.find_all(class_='freebirdFormviewerViewNumberedItemContainer')):
        qdata = re.findall(r'(?:\[\[)([0-9]*)', item.find(class_='m2').get('data-params'))
        if not qdata: continue
        data[f'entry.{qdata[0]}'] = input(
            f'\nQuestion {index+1}: '
            + item.find(class_='freebirdFormviewerComponentsQuestionBaseTitleDescContainer').find(class_='freebirdFormviewerComponentsQuestionBaseTitle').text
            + '\n'
        )
    if not data: raise Exception('No questions found.')

    # Send form submissions
    url = view_url[:-8]+'formResponse'
    match(input('\nReady to submit. Send continuously? (y/n)\n').lower()):
        case 'y'|'yes':
            print('\nSpamming continuous submissions...')
            while True: submit(url, data)
        case 'n'|'now':
            print('\nSending one submission...')
            submit(url, data)
        case _: raise Exception('Cancelled by user.')

if __name__ == '__main__':
    try: main()
    except Exception as error: print(error)