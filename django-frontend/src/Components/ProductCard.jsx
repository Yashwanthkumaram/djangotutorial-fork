import React from 'react';
import PropTypes from 'prop-types';
import { Card, CardContent, Typography, CardActions, Button, Rating } from '@mui/material';
import { CardMedia } from '@mui/material';

const ProductCard = ({ name, description, price, ratings ,image }) => {
    return (
        <Card>
            <CardContent>
                <CardMedia
                    component="img"
                    height="140"
                    image={image}
                    alt="product"/>
                <Typography variant="h5" component="div">
                    {name}
                </Typography>
                {/* <Typography variant="body2" color="text.secondary">
                    {description}
                </Typography> */}
                <Typography variant="h6" component="div">
                    Rs {price}
                </Typography>
                <Rating name="read-only" value={ratings} readOnly />
            </CardContent>
            <CardActions>
                <Button size="small">Add to Cart</Button>
            </CardActions>
        </Card>
    );
};

ProductCard.propTypes = {
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    ratings: PropTypes.number.isRequired,
    image : PropTypes.string.isRequired
};

export default ProductCard;