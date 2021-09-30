import React, { useContext } from 'react';
import { GlobalContext } from "../context/GlobalState";
import { Link } from "react-router-dom";
import {
  ListGroup,
  ListGroupItem,
  Button,
  Container
} from "reactstrap";

export const UserList = () => {
  const { users, removeUser } = useContext(GlobalContext);

  return (
    <ListGroup className="mt-4" >
      {users.length > 0 ? (
        <>
          {users.map(user => (
            <ListGroupItem className="d-flex" key={user.id} >
            
              <strong>{user.name}</strong>
              <Container>
                  <div class=" bd-highlight mb-1">
                    <div class="input-group" >
                      <div className="container">
                          <div className="row justify-content-end" >
                            <div className="col col-lg-2">
                              <Link  className="btn btn-warning mr-5" to={`/edit/${user.id}`} color="warning" >Edit</Link>
                            </div >
                            <div className="col-md-2" >
                              <Button onClick={() => removeUser(user.id)} color="danger">Delete</Button>
                            </div>
                          </div>
                        </div>
                      </div>  
                  </div>

              
              </Container>
              
            </ListGroupItem>
          ))}
        </>
      ) : (
          <h4 className="text-center">No Users</h4>
        )}
    </ListGroup>
  )
}