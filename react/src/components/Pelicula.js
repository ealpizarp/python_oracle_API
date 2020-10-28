import React from 'react'
import "bootstrap/dist/css/bootstrap.min.css"
import { Card } from 'react-bootstrap';
import { Button } from 'react-bootstrap';


class Pelicula extends React.Component{
    render(){
        return (
               <Card style={{ width: '18rem' }}>
                <Card.Img variant="top" src={this.props.Img} />
                <Card.Body>
                <Card.Title>{this.props.Title}</Card.Title>
                <Card.Text>
                     {this.props.Text} 
                </Card.Text>
                <Button variant="primary">Comprar</Button>
                </Card.Body>
                </Card>
        )


    }
}

export default Pelicula