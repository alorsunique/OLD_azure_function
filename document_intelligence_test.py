from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential


endpoint = "https://alorsdocumentintelligence.cognitiveservices.azure.com/"
api_key = "a98ca3abc8ed4e3187275808b034512d"

client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

url = "https://www.orimi.com/pdf-test.pdf"

poller = client.begin_analyze_document_from_url("prebuilt-document", document_url = url)
result = poller.result()

print(result)