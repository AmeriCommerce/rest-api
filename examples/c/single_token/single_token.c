#include <stdio.h>
#include <string.h>
#include <curl/curl.h>

// Self-signed cert
// #define SKIP_SSL_VERIFICATION 1

static size_t write_callback_func(void *buffer, size_t size, size_t nmemb, void *stream);

const char *STORE_DOMAIN = "<< YOUR STORE DOMAIN >>";
const char *ACCESS_TOKEN = "<< YOUR ACCESS TOKEN >>";

struct curl_slist *headers = NULL;

int main(void)
{
	CURL *curl;
	CURLcode response;
	char *data = NULL;
	char token_header[256];
	char endpoint_url[256];

	snprintf(token_header, sizeof(token_header), "X-AC-Auth-Token: %s", ACCESS_TOKEN);
	snprintf(endpoint_url, sizeof(endpoint_url), "https://%s/api/v1/products", STORE_DOMAIN);

	curl_global_init(CURL_GLOBAL_DEFAULT);

	curl = curl_easy_init();

	if(curl)
	{
		headers = curl_slist_append(headers, token_header);

		curl_easy_setopt(curl, CURLOPT_URL, endpoint_url);
		curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
		curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback_func);
		curl_easy_setopt(curl, CURLOPT_WRITEDATA, &data);

		#ifdef SKIP_SSL_VERIFICATION
			curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);
			curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0L);
		#endif

		response = curl_easy_perform(curl);

		if(response != CURLE_OK)
		{
			fprintf(stderr, "Get product list failed: %s\n", curl_easy_strerror(response));
		}

		curl_easy_cleanup(curl);
		curl_slist_free_all(headers);
	}

	curl_global_cleanup();

	printf("%s\n", data);

	return 0;
}

static size_t write_callback_func(void *buffer, size_t size, size_t nmemb, void *stream)
{
	char **response_ptr = (char**) stream;
	*response_ptr = strndup(buffer, (size_t)(size *nmemb));
	return strlen(*response_ptr);
}