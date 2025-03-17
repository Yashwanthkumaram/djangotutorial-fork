import React, { useState, useEffect, useContext } from 'react';
import ValidatingForm from "./email";
import { ThemeContext } from './themecontext';


import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';





import {
  Card,
  CardActionArea,
  CardContent,
  Typography,
  Avatar,
  Stack,
  Box,

  CircularProgress,
} from "@mui/material";

const MultiActionAreaCard = () => {

  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { theme } = useContext(ThemeContext);

  const darkTheme = createTheme({
    palette: {
      mode: theme.name,
    },
  });

  

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("https://dummyjson.com/users/?limit=1");
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const { users } = await response.json();
        setUser(users[0]);
      } catch (e) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

//   if (loading) {
//     return (
//       <Box
//         display="flex"
//         justifyContent="center"
//         alignItems="center"
//         minHeight="200px"
//       >
//         <CircularProgress />
//       </Box>
//     );
//   }
  if (loading){
    return(
        <>
        <Card
          lg={{
            maxWidth: 345,
            margin: "auto",
            width: { xs: "100%", md: "90%" },
            display: "flex",
            flexDirection: { xs: "column", md: "row" },
            alignItems: "center",
            boxSizing: "border-box",
          }}
        >
          <CardActionArea sx={{ display: "flex", width: "100%" }}>
            <Box
              sx={{
                padding: 2,
                display: "flex",
                justifyContent: "center",
                flex: 1,
                maxWidth: { xs: "100%", md: "150px" },
              }}
            >
            
                      <CircularProgress />

            </Box>
          </CardActionArea>
        </Card>
  
        
        <br/>
        <br/>
      
      </>
    )
  }

  if (error) {
    return <Typography color="error">Error: {error}</Typography>;
  }

  return (
      <ThemeProvider theme={darkTheme}>
                  <CssBaseline />
    <>

      <Card
        lg={{
          maxWidth: 345,
          margin: "auto",
          width: { xs: "100%", md: "90%" },
          display: "flex",
          flexDirection: { xs: "column", md: "row" },
          alignItems: "center",
          boxSizing: "border-box",
        }}
      >
        <CardActionArea sx={{ display: "flex", width: "100%" }}>
          <Box
            sx={{
              padding: 2,
              display: "flex",
              justifyContent: "center",
              flex: 1,
              maxWidth: { xs: "100%", md: "150px" },
            }}
          >
            <Avatar
              alt={`${user.firstName} ${user.lastName}`}
              src={user.image}
              sx={{ width: 150, height: 150 }}
            />
          </Box>
          <CardContent sx={{ flex: 2 }}>
            <Typography
              gutterBottom
              variant="h5"
              component="div"
              align="center"
            >
              {user.firstName} {user.lastName}
            </Typography>
            <Typography variant="body2" color="text.secondary" align="center">
              {`${user.company.title} - ${user.company.department}`}
              <br />
              {user.company.name}
              <br />
              {user.address.city}
              <br />
              {user.birthDate}
              <br />
              {user.email}
              <br />
              {user.username}
            </Typography>
          </CardContent>
        </CardActionArea>
      </Card>

      
      <br/>
        <br/>
    
    </>
    </ThemeProvider>
  );
};

export default MultiActionAreaCard;
