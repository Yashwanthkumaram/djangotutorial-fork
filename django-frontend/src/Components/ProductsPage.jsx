import React, { useState, useEffect } from "react";
import ProductCard from "./ProductCard";
import { 
  Box, 
  TextField, 
  MenuItem, 
  Select, 
  InputLabel, 
  FormControl, 
  Grid2, 
  Card, 
  CardMedia, 
  CardContent, 
  Typography, 
  Button 
} from "@mui/material";

const ProductsPage = () => {
  const [products, setProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("");
  const [sortBy, setSortBy] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const productsPerPage = 8;

  useEffect(() => {
    fetch("http://localhost:8000/api/products/")
      .then((res) => res.json())
      .then((data) => setProducts(data))
      .catch((err) => console.error("Error fetching products:", err));

    fetch("http://localhost:8000/api/categories/")
      .then((res) => res.json())
      .then((data) => setCategories(data))
      .catch((err) => console.error("Error fetching categories:", err));
  }, []);

  const getChildCategories = (parentId) => {
    const childCategories = categories
      .filter(category => category.parent_id == parentId)
      console.log(parentId, categories, childCategories);

    return [parentId, ...childCategories];

  };

  const filteredProducts = products
    .filter((product) => {
      const matchesSearch = product.p_name.toLowerCase().includes(searchTerm.toLowerCase());
      
      const matchesCategory = selectedCategory
        ? getChildCategories(selectedCategory).includes(product.cat_id)
        : true;
        
      return matchesSearch && matchesCategory;
    })
    .sort((a, b) => {
      if (sortBy === "priceLow") return a.price - b.price;
      if (sortBy === "priceHigh") return b.price - a.price;
      if (sortBy === "ratings") return b.ratings - a.ratings;
      return 0;
    });

  const indexOfLastProduct = currentPage * productsPerPage;
  const indexOfFirstProduct = indexOfLastProduct - productsPerPage;
  const currentProducts = filteredProducts.slice(indexOfFirstProduct, indexOfLastProduct);
  
  const totalPages = Math.ceil(filteredProducts.length / productsPerPage);

  return (
    <Box sx={{ padding: 3 }}>
      <Box sx={{ display: "flex", gap: 2, mb: 3 }}>
        <TextField
          label="Search Products"
          variant="outlined"
          fullWidth
          onChange={(e) => setSearchTerm(e.target.value)}
        />

        <FormControl sx={{ minWidth: 200 }}>
          <InputLabel>Category</InputLabel>
          <Select
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
          >
            <MenuItem value="">All</MenuItem>
            {categories.map((category) => (
              <MenuItem key={category.cat_id} value={category.cat_id}>
                {category.cat_name}
              </MenuItem>
            ))}
          </Select>
        </FormControl>

        <FormControl sx={{ minWidth: 200 }}>
          <InputLabel>Sort By</InputLabel>
          <Select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
          >
            <MenuItem value="">None</MenuItem>
            <MenuItem value="priceLow">Price: Low to High</MenuItem>
            <MenuItem value="priceHigh">Price: High to Low</MenuItem>
            <MenuItem value="ratings">Ratings</MenuItem>
          </Select>
        </FormControl>
      </Box>

      <Grid2 container spacing={3}>
        {currentProducts.length > 0 ? (
          currentProducts.map((product) => (
            <Grid2 item key={product.p_id} xs={12} sm={6} md={4} lg={3}>
              <ProductCard 
                name={product.p_name} 
                description={product.description} 
                price={product.price} 
                ratings={product.ratings} 
                image={product.image}
              /> </Grid2>
          ))
        ) : (
          <Typography variant="h6" sx={{ textAlign: "center", width: "100%" }}>
            No products found.
          </Typography>
        )}
      </Grid2>

      <Box sx={{ display: "flex", justifyContent: "center", mt: 4 }}>
        <Button 
          variant="contained" 
          disabled={currentPage === 1} 
          onClick={() => setCurrentPage((prev) => prev - 1)}
        >
          Previous
        </Button>
        <Typography variant="h6" sx={{ mx: 3 }}>
          Page {currentPage} of {totalPages}
        </Typography>
        <Button 
          variant="contained" 
          disabled={currentPage === totalPages} 
          onClick={() => setCurrentPage((prev) => prev + 1)}
        >
          Next
        </Button>
      </Box>
    </Box>
  );
};

export default ProductsPage;
