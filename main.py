from aleph_alpha_client import Client
from dotenv import dotenv_values

from app.query_api import classification, parse_results, retrieval
from app.scan import ocr, process_pdfs


def main():
    process_pdfs()
    ocr()

    # intitalize the alpeh alpha
    config = dotenv_values(".env")
    client = Client(token=config["AA_TOKEN"])

    # # get the classification
    results = classification(client)
    results = parse_results(results)
    results = retrieval(results, client)

    # save the results in a csv file
    results.to_csv("output/results.csv")


if __name__ == "__main__":
    main()
