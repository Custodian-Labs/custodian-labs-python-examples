# Usage note: every GuardianLayer call uses usage credits (bigger files use more) and counts
# toward your API key's request limit. The Free plan has limited monthly usage; check what's
# left in your Dashboard: https://dashboard.custodianlabs.io

from custodian_labs import GuardianLayer

# Mask personal data (PII) in a whole file and save a masked copy.
# Supported files: .csv, .xlsx, .xls, .docx, .pdf, .txt (picked by file extension).
# Run this script from the repo folder so the data_examples/ path is found.
# Docs: https://docs.custodianlabs.io/python-sdk/guardian-layer-client/

guardian = GuardianLayer()

input_file = "pii_data.csv"
# Try other file types too:
# input_file = "contract.pdf"
# input_file = "CV.docx"

result = guardian.deidentify_file(
    "data_examples/" + input_file,
    masking_type="transform",  # or "redact" / "placeholder" (see 01_simple_guardian_layer_text.py)
    pii_entities=["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER"],  # cities are left as-is
)

# Save the masked copy next to where you ran the script
output_file = "masked_" + input_file
with open(output_file, "wb") as f:
    f.write(result.content)
print("Saved masked file:", output_file)

# Text files can be previewed right here; open PDF/DOCX files to compare
if input_file.endswith((".csv", ".txt")):
    print(result.text())
