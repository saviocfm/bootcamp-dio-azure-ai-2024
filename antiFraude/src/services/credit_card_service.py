from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config 

def analize_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.SUBSCRIPTION_KEY)
        document__client = DocumentIntelligenceClient(Config.ENDPOINT,credential)
        card_info =  document__client.begin_analyze_document("prebuild-creditCard",AnalyzeDocumentRequest(url_source=card_url))
        result = card_info.result()
        return result 
    except Exception as ex: 
        return None