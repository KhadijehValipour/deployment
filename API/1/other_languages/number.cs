var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Get, "http://numbersapi.com/42");
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
