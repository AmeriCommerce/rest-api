use REST::Client;
use JSON;

my $STORE_DOMAIN = '<< YOUR STORE DOMAIN >>';
my $ACCESS_TOKEN = '<< YOUR ACCESS TOKEN >>';

# If using a dev cert
# $ENV{PERL_LWP_SSL_VERIFY_HOSTNAME}=0;

my $headers = {
	'X-AC-Auth-Token' => $ACCESS_TOKEN
};
my $client = REST::Client->new();

$client->setHost('https://' . $STORE_DOMAIN);
$client->GET('/api/v1/products', $headers);

my $response = from_json($client->responseContent());
my $products = $response->{'products'};

foreach $product (@$products) {
	my $itemName = $product->{'item_name'};
	my $price = $product->{'price'};

	print $itemName . ": " . $price . "\n";
}