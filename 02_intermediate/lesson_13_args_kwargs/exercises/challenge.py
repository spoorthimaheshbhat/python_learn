def generate_report(report_name, *scores, **metadata):
    print(f"Report name: {report_name}")

    print("Scores:")

    for score in scores:
        print(score)

    print(f"\nAverage: {round(sum(scores)/len(scores),2)}")

    print(f"\nMetadata:")
    for key, value in metadata.items():
        print(f"{key} : {value}")

generate_report(
    "Python Assessment",
    80,
    90,
    75,
    trainer="John",
    batch="2026"
)




