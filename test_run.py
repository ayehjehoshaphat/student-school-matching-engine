for school, score, explanation in results:
    print(f"\n{school}")
    print(f"Score: {score}")
    print("Breakdown:")
    for k, v in explanation.items():
        print(f" - {k}: {v}")
