Uploading Files
===============

Files can be uploaded using `POST /api/v1/upload`. This endpoint accepts requests with the `Content-Type: multipart/form-data`. There are two parts supported in this multipart request: an `application/json` part and the payload part.

A sample request to this endpoint would look like the following:

```shell
POST https://samplestore.americommerce.com/api/v1/upload HTTP/1.1
X-AC-Auth-Token: <access_token>
Content-Type: multipart/form-data; boundary="Cart.com API demo"
Host: samplestore.americommerce.com
Content-Length: 287054
Connection: Keep-Alive

--Online Store API demo
Content-Type: application/json
Content-Disposition: form-data

{"destination":"/shared/images/sample.jpg","overwrite":true}
--Online Store API demo
Content-Type: image/jpeg
Content-Disposition: form-data

<binary_data>
--Online Store API demo--
```

The `Content-Type` of the overall request should be set to `multipart/form-data`. This is also where we will need to specify what the boundary string is for the multipart request. The boundary will tell the server where one part begins and ends.

The body of the request starts with the boundary string prefixed with two dashes. On the next line, we specify the `Content-Type` of the first part, which should be `application/json`. In this section, we supply a JSON object representing the options to pass to the file upload action.

After our JSON section, another boundary is added. Then we specify a section with the `Content-Type` set to the MIME type of our file; in this case, a JPEG file.

Following the headers for this section will be the binary data for the file. After the binary data, there is a closing boundary, which has two dashes as a prefix AND a suffix. The suffix indicates the end of the request.

A successful file upload request will return `204 No Content`.

File Upload Options
-------------------

* `destination` - (required) The path (relative to the root of the site) where the file will be uploaded and what the file should be named, i.e. `/shared/images/sample.jpg`
* `overwrite` - (optional) Flag that specifies whether or not an existing file at the destination path should be overwritten.

Encoding Binary Data
--------------------

There is an alternate method for submitting the binary data for the file you want to upload. You have the option of base64 encoding the data and submitting it as a string on the request. To do this, add the additional header `Content-Transfer-Encoding: base64`.

Sample Code
-----------

### C# Sample Code

This code will produce the sample request shown above and print out the resulting status code.

```csharp
var webService = new Uri("https://samplestore.americommerce.com/api/v1/upload");
var requestMessage = new HttpRequestMessage(HttpMethod.Post, webService);

requestMessage.Headers.ExpectContinue = false;
requestMessage.Headers.Add("X-AC-Auth-Token", "<access_token>");

var multiPartContent = new MultipartFormDataContent("AmeriCommerce API demo");
var json = "{\"destination\":\"/shared/images/sample.jpg\",\"overwrite\":true}";
var fileData = File.ReadAllBytes("sample.jpg");

var jsonContent = new StringContent(json);
jsonContent.Headers.ContentType = MediaTypeHeaderValue.Parse("application/json");
multiPartContent.Add(jsonContent);

var binaryContent = new ByteArrayContent(fileData);
binaryContent.Headers.ContentType = MediaTypeHeaderValue.Parse("image/jpeg");
multiPartContent.Add(binaryContent);

requestMessage.Content = multiPartContent;

var httpClient = new HttpClient();
var httpRequest = httpClient.SendAsync(requestMessage, HttpCompletionOptions.ResponseContentRead);
var httpResponse = httpRequest.Result;

Console.WriteLine(httpResponse.StatusCode);
```
