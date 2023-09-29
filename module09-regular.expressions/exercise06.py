import re

contact = "Kate Austen,Gsm: +90-212-555-1248,Home: +90-216-444-9854,Work: +90-555-111-2345"
phones = re.findall("((Gsm|Home|Work): (\+\d{1,3}-\d{1,3}-\d{3}-\d{4}))", contact)
print(phones)
for phone in phones:
    if phone[1] == "Home":
        print(f"Dialing {phone[2]}...")
