import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import ContextualCompressionFilterClient

def main():
    client = ContextualCompressionFilterClient()
    res = client.compress_document_context()
    print("=== Contextual Compression Filter Output ===")
    print(f"Original Words: {res['original_word_count']} -> Compressed: {res['compressed_word_count']} (Ratio: {res['compression_ratio']})")
    print(f"Estimated Tokens Saved: ~{res['tokens_saved_estimate']}")
    print("\nRetained Context Snippets:")
    for s in res['retained_snippets']:
        print(f"  - [{s['relevance_score']}] {s['snippet']}")

if __name__ == '__main__':
    main()
