import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="alors_http_trigger")
def alors_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    pdfurl = req.params.get('pdfurl')
    if not pdfurl:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            pdfurl = req_body.get('pdfurl')

    if pdfurl:

        from azure.ai.formrecognizer import DocumentAnalysisClient
        from azure.core.credentials import AzureKeyCredential


        endpoint = "https://alorsdocumentintelligence.cognitiveservices.azure.com/"
        api_key = "a98ca3abc8ed4e3187275808b034512d"

        client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

        url = pdfurl

        poller = client.begin_analyze_document_from_url("prebuilt-document", document_url = url)
        result = poller.result()

        

        result_dict = result.to_dict()

        #print(f"PDF Content\n{result.content}\n\n")
        #print(f"Complete Poller Results\n{result_dict}")


        output= f"PDF Content\n\n{result.content}\n\n\n\nComplete Poller Results\n\n{result_dict}"

        #return func.HttpResponse(f"Hello, {pdfurl}. This HTTP triggered function executed successfully. Nice to meet you {pdfurl}.")
    
        return func.HttpResponse(output, status_code=200)


    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a PDF url in the query string as &pdfurl=.",
             status_code=200
        )