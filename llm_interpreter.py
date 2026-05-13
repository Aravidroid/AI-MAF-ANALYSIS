import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def explain_results(results):

    prompt = f"""
You are a cancer genomics AI assistant.

Analyze the following mutation analysis results and generate a CLEAN,
PROFESSIONAL markdown report.

DATA:
- Total Mutations: {results['total_mutations']}

- Top Mutated Genes:
{results['top_genes']}

- Variant Classifications:
{results['variant_types']}

FORMAT RULES:
- Use markdown headings
- Use bullet points
- Keep paragraphs SHORT
- Avoid giant walls of text
- Make the report readable
- Use simple scientific language
- Maximum 300 words

Generate sections in this order:

# Mutation Summary
Short overview.

# Key Gene Findings
Explain major mutated genes.

# Variant Classification Insights
Explain important mutation types.

# Biological Significance
Possible biological meaning.

# Cancer Relevance
Potential cancer associations.

# Final Research Summary
Short concluding summary.
"""

    response = model.generate_content(prompt)

    return response.text