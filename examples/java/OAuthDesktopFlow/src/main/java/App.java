public class App {

    public static void main(String[] args) {

        AmeriCommerceApi api = new AmeriCommerceApi();

        try {

            OAuthVerifyResponseModel token = api.getToken("<< USER NAME >>", "<< USER API KEY >>");

            ProductList list = api.getProductList(token.getAccessToken());

            for(Product p : list.getProducts()) {
                System.out.println(p.getItemName() + ": " + p.getPrice());
            }

        } catch (Exception ex) {
            ex.printStackTrace();
        }

    }

}
