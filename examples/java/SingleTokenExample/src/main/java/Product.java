public class Product {
    private int _id;
    private String _itemName;
    private String _itemNumber;
    private double _price;

    public int getId() {
        return _id;
    }
    public void setId(int _id) {
        this._id = _id;
    }

    public String getItemName() {
        return _itemName;
    }
    public void setItemName(String value) {
        this._itemName = value;
    }

    public String getItemNumber() {
        return _itemNumber;
    }
    public void setItemNumber(String value) {
        this._itemNumber = value;
    }

    public double getPrice() {
        return _price;
    }
    public void setPrice(double value) {
        this._price = value;
    }
}
