def generate_answer(query, context):
    """
    Generates a structured answer using retrieved context.
    This is a fallback version (no external API required).
    """

    # If no context found
    if not context or not context.strip():
        return "❌ No relevant data found in the codebase."

    # Trim context to avoid too large output
    trimmed_context = context[:1000]

    # Generate structured response
    answer = f"""
🔍 **Query:**
{query}

📘 **Relevant Code Snippets:**
{trimmed_context}

💡 **Explanation:**
The system performed semantic search on the repository using vector embeddings.
It retrieved the most relevant code sections related to your query and displayed them above.

This helps developers quickly understand large codebases without manually reading every file.
"""

    return answer