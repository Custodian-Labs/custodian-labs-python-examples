# Application Examples

Real-world AI agents built with the [`custodian-labs`](https://pypi.org/project/custodian-labs/) SDK. Each one is a single script you can run, then adapt to your own use case.

New to the SDK? Start with the numbered examples (`01`–`03`) in the [repo root](../README.md) first.

| File | Use case |
|---|---|
| `legal_contract_assistant.py` | Legal assistant that answers questions about a contract (PDF) |
| `cv_recruiter_assistant.py` | Share an AI agent that answers recruiters' questions about your CV (DOCX) |

## Running an example

Run from the **repo root** so the `data_examples/` paths resolve:

```bash
python application_examples/legal_contract_assistant.py
```

Each example deploys a new Custodian. On the Free plan you can have 1 deployed at a time, so delete the previous one under **My AIs** in the [Dashboard](https://dashboard.custodianlabs.io) before running another.

---

## Submit your own example

Built something useful? Share it so others can learn from it.

1. **Fork** [Custodian-Labs/custodian-labs-python](https://github.com/Custodian-Labs/custodian-labs-python) on GitHub, then clone your fork:
   ```bash
   git clone https://github.com/<your-username>/custodian-labs-python.git
   cd custodian-labs-python
   ```
2. **Create a branch:**
   ```bash
   git checkout -b add-<your-use-case>
   ```
3. **Copy the template** and fill in each `TODO`:
   ```bash
   cp application_examples/_template.py application_examples/<your_use_case>.py
   ```
   Use a short, descriptive file name in `snake_case`, e.g. `restaurant_menu_assistant.py`.
4. **Add any data file** to `data_examples/`. It must be fictional or publicly available.
5. **Run it** from the repo root and check it works end to end.
6. **Add a row** for your example to the table above.
7. **Push and open a pull request** against `main`, with a one-line description of the use case.

### Guidelines

- **No real personal data.** Use made-up names, `example.com` emails and `555` phone numbers.
- **No API keys or secrets** in code. The SDK reads your key from `CUSTODIAN_SDK_API_KEY`.
- **Keep it to one file**, with comments a beginner can follow.
- **Run on the Free plan** where possible (`gpt-4o`, a single Custodian), so anyone can try it.
