import requests
import urllib


requested = "hi there"
r = requests.get(f"https://ulesa.cognitiveservices.azure.com/bing/v7.0/suggestions/?{urllib.parse.quote_plus(requested)}", {
	"headers": {
		"Ocp-Apim-Subscription-Key": "4b3f89575494450dbc948e2d6fe427e2"
	}
})
print(r, r.content)