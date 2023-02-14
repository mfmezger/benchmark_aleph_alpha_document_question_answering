import json
import os

import pandas as pd
from aleph_alpha_client import CompletionRequest, Prompt


def classification(client) -> dict:
    # get the prompt from the prompt folder
    results = {}

    with open("prompts/PROMPT_Document_classification.txt") as f:
        prompt = f.read()

    # iterate over the folders
    for folder in os.listdir("output"):
        # get the file with a 0 in the name
        for file in os.listdir(f"output/{folder}"):
            if "_0" in file:
                # get the text from the file
                with open(f"output/{folder}/{file}") as f:
                    text = f.read()

                # do classification with the prompt and the text
                request = CompletionRequest(
                    prompt=Prompt.from_text(
                        f"""
                {prompt}
                Document:
                {text}
                ###
                Q: Document category A: """
                    ),
                    maximum_tokens=3,
                    stop_sequences=["###"],
                )
                response = client.complete(request, model="luminous-extended")

                response = response.completions[0].completion

                # save the classification in the results dictionary
                results[folder] = response

    return results


def parse_results(results) -> dict:
    parsed_results = {}
    # load the class defintions from class_definitions/classes.json
    with open("class_definition/classes.json") as f:
        classes = json.loads(f.read())

    # iterate over the results
    for key, value in results.items():
        # iterate over the classes from the json file
        for cla in classes:
            # remove the \n from the value
            clean_value = value.replace("\n", "")
            # remove starting and ending spaces
            clean_value = clean_value.strip()
            # if the class is in the results, add it to the parsed_results
            if clean_value.lower() in classes[cla]:
                parsed_results[key] = cla

    return parsed_results


def retrieval(results, client):
    # create pandas dataframe from the results
    df = pd.DataFrame(columns=["name", "classification", "retrieval"])
    # iterate over the results
    for key, value in results.items():
        # get the prompt with the same number as in value.
        with open(f"prompts/PROMPT_Document_class_{value}.txt") as f:
            prompt = f.read()

        # replace the {} in the prompt with the text from the file
        with open(f"output/{key}/{key}_0.txt") as f:
            text = f.read()

        prompt = prompt.replace("{}", text)

        request = CompletionRequest(prompt=Prompt.from_text(prompt), maximum_tokens=30, stop_sequences=["###"])
        response = client.complete(request, model="luminous-extended")

        response = response.completions[0].completion

        # add the results to the dataframe
        df = df.append(
            {
                "name": key,
                "classification": value,
                "retrieval": response,
            },
            ignore_index=True,
        )

    return df
