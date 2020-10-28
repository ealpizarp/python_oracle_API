import React from 'react'
import { Navbar } from 'react-bootstrap';
import { Nav } from 'react-bootstrap';
import "bootstrap/dist/css/bootstrap.min.css"

class Bar extends React.Component{
    render(){
        return (
            <Navbar bg="dark" variant="dark">
            <Navbar.Brand href="#home">Cine Lup</Navbar.Brand>
            <Nav className="mr-auto">
              <Nav.Link href="#features">Peliculas</Nav.Link>
              <Nav.Link href="#pricing">Registrarse</Nav.Link>
            </Nav>
           
          </Navbar>
        )


    }
}

export default Bar