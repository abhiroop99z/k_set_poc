import React, { useContext, useState, useEffect, useRef } from "react";
import "./Searchbar.css";

import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import NavDropdown from "react-bootstrap/NavDropdown";
import Form from "react-bootstrap/Form";
import FormControl from "react-bootstrap/FormControl";
import Button from "react-bootstrap/Button";

import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";

import { FetchDataContext } from "../../Context/FetchDataContext";

function SearchBar() {
  var path = "Path to be sent by the backend.";
  const {
    OnSubmit,
    getData,
    setSearchQuery,
    setSearchTarget,
    searchQuery,
    allTarget
  } = useContext(FetchDataContext);

  const [setTitle, isSetTitle] = useState("");
  const [setValue, isSetValue] = useState("");
  const [isSuggestion, setIsSuggestion] = useState([]);
  const [allTargetList, setAllTargetList] = useState([]);
  const [isExpanded, setIsExpanded] = useState(false);
  const wrapperRef = useRef(null);
  const [isSuggestionVisible, setIsSuggestionVisible] = useState(false);

  {
    // getData != null ? (path = getData["Path"]) : (path = null); When actual data will come from backend use this.
    getData != null ? (path = getData["Path"]) : (path = path);
  }

  // Assign value of the search query.

  const suggestHandler = event => {
    // console.log(event)
    setIsExpanded(false);
    isSetValue(event);
    setSearchQuery(event);
    setIsSuggestion([]);
  };

  const submitData = event => {
    setIsSuggestion([]);
    console.log("here");

    const timer = setTimeout(() => {
      OnSubmit();
    }, 1000);

    return () => {
      clearTimeout(timer);
    };
  };

  const handleTextChange = e => {
    e.preventDefault();
    const text = e.target.value;
    setSearchQuery(e.target.value);
    isSetValue(text);

    // setIsExpanded(true);

    // Call the API after 3 sec of key stroke (or say when user stops typing for 3 secs).
    // setTimeout(() => {
    //   suggest();
    // });
  };

  // Show or hide the suggestions.

  // const handleClickOutside = event => {

  //   if (wrapperRef.current == event.target) {
  //     setIsSuggestionVisible(true);
  //   } else {
  //     setIsSuggestionVisible(false);
  //   }
  // };

  // useEffect(() => {
  //   document.addEventListener("click", handleClickOutside, false);
  //   return () => {
  //     document.removeEventListener("click", handleClickOutside, false);
  //   };
  // });

  // Call the API after 3 sec of key stroke (or say when user stops typing for 3 secs).

  // Disable the suggestions for now.
  // useEffect(() => {
  //   async function suggest() {
  //     const DATA_FORMAT = {
  //       query: searchQuery
  //     };

  //     const response = await fetch(`${process.env.REACT_APP_URL}dummy`, {
  //       method: "POST",
  //       headers: {
  //         "Content-Type": "application/json"
  //       },

  //       body: JSON.stringify(DATA_FORMAT)
  //     });
  //     const json = await response.json();
  //     setIsSuggestion(json);
  //   }

  //   const timer = setTimeout(() => {
  //     if (!isExpanded) {
  //       setIsExpanded(true);
  //     } else {
  //       suggest();
  //     }
  //   }, 1000);

  //   return () => {
  //     clearTimeout(timer);
  //   };
  // }, [setValue]);

  // Ends.

  // Assign the value of dropdown.
  const handleSelect = (eventKey, e) => {
    setSearchTarget(eventKey);
    isSetTitle(e.target.textContent);
  };

  // Fetch list of all the targets.

  // useEffect(async () => {
  //   const response = await allTarget();
  //   // console.log(response)
  //   setAllTargetList(response);
  // }, []);
  // Return the view.

  return (
    <div className="container-fluid">
      <Navbar bg="" expand="lg" className="customSearchNav">
        <Container fluid>
          <Navbar.Toggle aria-controls="navbarScroll" />
          <Navbar.Collapse id="navbarScroll">
            <Nav
              className="me-auto my-2 my-lg-4"
              style={{ maxHeight: "100px" }}
              navbarScroll
            ></Nav>
            <Form className="d-flex">
              <FormControl
                type="search"
                placeholder="Search..."
                className="me-2"
                aria-label="Search"
                id="form"
                onChange={handleTextChange}
                autoComplete="off"
                value={setValue}
                ref={wrapperRef}
              />
              {/* Add suggesion code here from suggestion component when the issue gets resolved. */}
              {/* {isSuggestionVisible && ( */}
              <div className="toggleSuggestion">
                {/* Show if suggestions are available */}
                {/* Auto suggestion based on user input */}
                {Object.entries(isSuggestion).length !== 0 &&
                  searchQuery !== "" && (
                    <Card className="suggestionClass" ref={wrapperRef}>
                      {Object.entries(isSuggestion).map(([key, value]) => {
                        return value.map(e => {
                          return (
                            <ListGroup
                              onClick={() => suggestHandler(key)}
                              className="suggestionClassList"
                            >
                              <ListGroup.Item className="ListGroup">
                                <p className={"key"}>{key}</p>
                                <p className="cardValue">{e}</p>
                              </ListGroup.Item>
                            </ListGroup>
                          );
                        });
                      })}
                    </Card>
                  )}
              </div>
              {/* )} */}
            </Form>

            <NavDropdown
              title={setTitle || "Categories"}
              id="navbarScrollingDropdown"
              className="dropDownButton"
              onSelect={handleSelect}
            >
              {/* <NavDropdown.Item eventKey="case_studies">
                Case Studies
              </NavDropdown.Item>
              <NavDropdown.Item eventKey="proposals">
                Proposals
              </NavDropdown.Item> */}
              {/* <NavDropdown.Divider /> */}
              {/* <NavDropdown.Item eventKey="All">All</NavDropdown.Item> */}
              {/* <NavDropdown.Item eventKey="document">Document</NavDropdown.Item> */}
              <NavDropdown.Item eventKey="company">Company</NavDropdown.Item>
              {/* <NavDropdown.Item eventKey="vertical">Vertical</NavDropdown.Item>
              <NavDropdown.Item eventKey="feedback">Feedback</NavDropdown.Item>
              <NavDropdown.Item eventKey="engagement_details">Engagement Details</NavDropdown.Item>
              <NavDropdown.Item eventKey="technology_focus">Technology Focus</NavDropdown.Item>
              <NavDropdown.Item eventKey="venture_capitalist">Venture Capitalist</NavDropdown.Item>
              <NavDropdown.Item eventKey="active_customers">Active Customers</NavDropdown.Item>
              <NavDropdown.Item eventKey="zensar_customer">Zensar Customer</NavDropdown.Item> */}

              {/* {Object.entries(allTargetList).map(([k, v], index) => {
                return <NavDropdown.Item eventKey={v}>{k}</NavDropdown.Item>;
                
              })} */}
            </NavDropdown>
            <Button
              variant="outline-success"
              className="searchButton"
              // onClick={OnSubmit}
              onClick={submitData}
            >
              Search
            </Button>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </div>
  );
}

export default SearchBar;
