import java.util.Collection;

public class ProductList {
    private int _totalCount;
    private String _nextPage;
    private String _previousPage;
    private Collection<Product> _products;

    public int getTotalCount() {
        return _totalCount;
    }
    public void setTotalCount(int value) {
        _totalCount = value;
    }

    public String getNextPage() {
        return _nextPage;
    }
    public void setNextPage(String value) {
        _nextPage = value;
    }

    public String getPreviousPage() {
        return _previousPage;
    }
    public void setPreviousPage(String value) {
        _previousPage = value;
    }

    public Collection<Product> getProducts() {
        return _products;
    }
    public void setProducts(Collection<Product> value) {
        _products = value;
    }
}