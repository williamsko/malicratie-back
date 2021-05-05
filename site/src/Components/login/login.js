import logoMalicratie from '../Navbar/logoMalicratie.svg';



import React from 'react';
import './login.css';
import {Form,Button}from 'react-bootstrap';
class Login extends React.Component{
    render (){
        return (
            <div id="loginContainer"className="container-fluid">
             

                <Form id="loginform">
                <img id="logo_login" src={logoMalicratie} alt="Logo Malicratie"/>
                        <Form.Group controlId="formBasicEmail">
                            <Form.Control type="email" placeholder="Enter email" />
                            <Form.Text className="text-muted">

                            </Form.Text>
                        </Form.Group>

                        <Form.Group controlId="formBasicPassword">
                            <Form.Control type="password" placeholder="Password" />
                        </Form.Group>
                        <Form.Group controlId="formBasicCheckbox">
                            <Form.Check type="checkbox" label="Rester connecté" />
                        </Form.Group>
                        <Button id ="btnConnexion"variant="success" type="submit">
                            Se Connecter
                        </Button>
                </Form>
            </div>
        )
    }
}

export default Login;