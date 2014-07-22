package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

const storeDomain = "<< YOUR STORE DOMAIN >>"
const accessToken = "<< YOUR ACCESS TOKEN >>"

type Product struct {
	ItemName string `json:"item_name"`
	Price    float64
}

type ProductList struct {
	NextPage     string `json:"next_page"`
	PreviousPage string `json:"previous_page"`
	TotalCount   int    `json:"total_count"`
	Products     []Product
}

func getProductList() (*ProductList, error) {
	req, err := http.NewRequest("GET", fmt.Sprintf("https://%s/api/v1/products", storeDomain), nil)
	if err != nil {
		return nil, err
	}
	req.Header.Add("X-AC-Auth-Token", accessToken)

	client := new(http.Client)
	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	var list ProductList
	err = json.Unmarshal(body, &list)
	if err != nil {
		return nil, err
	}
	return &list, err
}

func main() {
	list, err := getProductList()
	if err != nil {
		fmt.Println(err)
	} else {
		for _, p := range list.Products {
			fmt.Println(p.ItemName+":", p.Price)
		}
	}
}
