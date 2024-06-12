import React, { useContext, Fragment } from "react";
import Navbar from "../../Components/Navbar/Navbar";
import Searchbar from "../../Components/SearchBar/Searchbar";
import RenderContent from "../../Containers/RenderContent/RenderContent";
import RenderFilter from "../../Containers/RenderFilter/RenderFilter";
import { FetchDataContext } from "../../Context/FetchDataContext";
import { PaginationContextProvider } from "../../Context/PaginationContext";

import Loading from "../../Components/Loading/Loading";

import styles from "./Screen.module.css";
import Col from "react-bootstrap/Col";

function Screen() {
  const { dataFromAPI, isLoading } = useContext(FetchDataContext);
  return (
    <Fragment>
      <div>
        {/* Top bar for rendring the logo */}
        <Navbar />
      </div>

      <div className="container-fluid">
        <div className="row">
          {/* PaginationContextProvider enables the pagination to show multiple data in different pages. */}
          <PaginationContextProvider>
            {/* Show the filters only when the user has searched for the query and the data from the API is not null. */}
            <Col xs={4} sm={4} md={3} lg={2}>
              {dataFromAPI != null ? <RenderFilter /> : null}
            </Col>
            <Col xs={8} sm={8} md={9} lg={10}>
              {/* Show the search bar always, but show the content only when the data from the API has arrived and data is not null. */}
              <Searchbar />
              {isLoading === true ? (
                <div>
                  {/* Loading... */}
                  <Loading />
                </div>
              ) : dataFromAPI != null ? (
                <RenderContent />
              ) : null}
            </Col>
          </PaginationContextProvider>
        </div>
      </div>
    </Fragment>
  );
}

export default Screen;
