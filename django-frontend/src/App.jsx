import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ProductsPage from './Components/ProductsPage';


const App = () => {
    return (
        <BrowserRouter>
        <Routes>
          <Route index element={<ProductsPage />} />
          <Route path="/products" element={<ProductsPage />} />
        </Routes>
      </BrowserRouter>
    );
};

export default App;