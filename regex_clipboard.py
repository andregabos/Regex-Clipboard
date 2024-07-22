#! python3

import re
import pyperclip
import argparse

def extract_urls(text):
    url_pattern = r'https?://\S+'
    urls = re.findall(url_pattern, text)
    return '\n'.join(urls)

def standardize_dates(text):
    date_pattern = r'(\d{1,4})[/-](\d{1,2})[/-](\d{1,4})'
    def standardize_date(match):
        year, month, day = sorted(match.groups(), key=len, reverse=True)
        return f"{year}-{month:0>2}-{day:0>2}"
    return re.sub(date_pattern, standardize_date, text)

def remove_sensitive_info(text):
    ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
    credit_card_pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    text = re.sub(ssn_pattern, '[SSN REMOVED]', text)
    return re.sub(credit_card_pattern, '[CREDIT CARD REMOVED]', text)

def fix_typos(text):
    multiple_spaces_pattern = r'\s{2,}'
    repeated_words_pattern = r'\b(\w+)\s+\1\b'
    multiple_exclamations_pattern = r'!{2,}'
    text = re.sub(multiple_spaces_pattern, ' ', text)
    text = re.sub(repeated_words_pattern, r'\1', text)
    return re.sub(multiple_exclamations_pattern, '!', text)

#def extract_phones(text):
    phone_pattern = r'\b(?:\+?1[-.\s]?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}\b'
    phones = re.findall(phone_pattern, text)
    return '\n'.join(phones)

def extract_phones(text):
    phone_pattern = r'''
    (?:
        (?:\+?55\s?)? 
        (?:\(?0?[1-9]{2}\)?)? 
        \s?
        (?:
            9?[6-9]\d{3}[-.\s]?\d{4} | 
            [2-5]\d{3}[-.\s]?\d{4} 
        )
    )
    '''
    phones = re.findall(phone_pattern, text, re.VERBOSE)
    return '\n'.join(phones)

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return '\n'.join(emails)


def main():
    parser = argparse.ArgumentParser(description="Apply regex patterns to clipboard text.")
    parser.add_argument('operation', choices=['urls', 'dates', 'sensitive', 'typos', 'all', 'phones', 'emails'],
                        help="Specify which operation to perform")
    args = parser.parse_args()

  
    text = pyperclip.paste()

    if args.operation == 'urls':
        result = extract_urls(text)
    elif args.operation == 'dates':
        result = standardize_dates(text)
    elif args.operation == 'sensitive':
        result = remove_sensitive_info(text)
    elif args.operation == 'typos':
        result = fix_typos(text)
    elif args.operation == 'phones':
        result = extract_phones(text)
    elif args.operation == 'emails':
        result = extract_emails(text)

 
    pyperclip.copy(result)
    print(f"Operation '{args.operation}' applied successfully. Result copied to clipboard.")

if __name__ == "__main__":
    main()