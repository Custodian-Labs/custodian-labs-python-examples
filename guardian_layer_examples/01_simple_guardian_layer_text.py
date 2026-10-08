# Usage note: every GuardianLayer call uses usage credits (bigger inputs use more) and counts
# toward your API key's request limit. This script makes 4 calls. The Free plan has limited
# monthly usage; check what's left in your Dashboard: https://dashboard.custodianlabs.io

from custodian_labs import GuardianLayer

# GuardianLayer finds personal data (PII) in text and masks it, before you store it
# or send it to an AI model. It's separate from AI agents but uses the same API key.
# Docs: https://docs.custodianlabs.io/python-sdk/guardian-layer-client/

guardian = GuardianLayer()

text = "John Smith lives in Boston and his phone number is 617-555-0100."

# 1. Find the sensitive words
analysis = guardian.analyze_proprietary(text)
print("Sensitive words:", analysis.sensitive_words)

# 2. Mask them. Compare the three masking styles:
#   redact      -> replaces PII with *****
#   placeholder -> replaces PII with labels like [NAME], [PHONE]
#   transform   -> replaces PII with similar stand-in words
for masking_type in ["redact", "placeholder", "transform"]:
    result = guardian.deidentify_text_outputs(
        text,
        masking_type=masking_type,
        pii_entities=["ALL"],  # or a list, e.g. ["PERSON", "PHONE_NUMBER", "EMAIL_ADDRESS", "LOCATION"]
    )
    print(f"\n{masking_type}:", result.outputs[0].text)
# transform also returns a second alternative in result.outputs[1]
