import React, { useContext } from 'react';
import { AppBar, Toolbar, Typography, Button, IconButton } from '@mui/material';
import { ThemeContext } from './themecontext';
import Box from '@mui/material/Box';
import { Link } from 'react-router-dom';


const Navbar = () => {
    const { theme, setTheme } = useContext(ThemeContext);
    const navItems = ['Profile', 'Employee'];

    const toggleTheme = () => {
        setTheme((prevTheme) => ({
            ...prevTheme,
            name: prevTheme.name === 'light' ? 'dark' : 'light',
            background: prevTheme.name === 'light' ? '#333333' : '#ffffff',
            foreground: prevTheme.name === 'light' ? '#ffffff' : '#000000',
        }));
    };

    return (
        <AppBar position="static">
            <Toolbar>
            <Box sx={{ display: { xs: 'none', sm: 'block' } }}>
              {navItems.map((item) => (
                <Button key={item} sx={{ color: '#fff' }}>
                  <Link to={`/${item}`} style={{ color: '#fff', textDecoration: 'none' }}>
                    {item}
                  </Link>
                </Button>
              ))}
            </Box>
                <Button color="inherit" onClick={toggleTheme}>
                    {theme.name === 'light' ? 'Dark Mode' : 'Light Mode'}
                </Button>
            </Toolbar>
        </AppBar>

    );
};

export default Navbar;

