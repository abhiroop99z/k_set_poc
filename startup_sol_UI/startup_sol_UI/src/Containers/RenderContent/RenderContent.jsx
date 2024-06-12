import React, { useContext, Fragment, useState } from "react";
import { FetchDataContext } from "../../Context/FetchDataContext";
import Content from "../../Components/Content/Content";

import styles from "./RenderContent.module.css";
import ReactPaginate from "react-paginate";
import Card from "react-bootstrap/Card";
import Container from "react-bootstrap/Container";
function createCard(data) {
  // var Conference_name = data.Conference_name.replace('/', "");
  return (
    <Content
      // To be used for this UI.
      // title={data.name}
      // link={data.document_link}
      // customerName={data.customer_name}
      // pillar={data.pillar}
      // publicationDate={data.created_date}
      // serviceType={data.type_of_service}
      // region={data.region}
      // vertical={data.vertical}
      // path = {data.shortest_path}

      // Only for testing of dynamic data render. Can delete later on.

      // document={data.name}
      // uuid={data.doc_uuid}
      // assetType={data.asset}
      // channel={data.channel}
      // area={data.area}
      // collection={data.collection}
      // subject={data.subject}
      // technology={data.technology}
      // description={data.description}

      companyName={data.company_name}
      city={data.city}
      state={data.state}
      country={data.country}
      technologyFocus={data.has_technology_focus}
      engagementDetails={data.has_eng_details}
      vertical={data.has_vertical}
      activeCustomers={data.has_customers}
      usecase={data.has_usecase}
      venture={data.has_venture}
      zensarCustomers={data.has_customers}

      // company = {data}
    />
  );
}

function RenderContent() {
  const { dataFromAPI } = useContext(FetchDataContext);
  var x = dataFromAPI["paper_res"];
  const [pageNumber, setPageNumber] = useState(0);
  const userPerPage = 10;
  const pagesVisited = pageNumber * userPerPage;
  const pageCount = Math.ceil(x.length / userPerPage);

  const v = x.slice(pagesVisited, pagesVisited + userPerPage);
  const pageChange = ({ selected }) => {
    setPageNumber(selected);
  };
  return (
    <Fragment>
      {/* If no data is found or the data from the API is null, send the custom message to the UI. */}
      {x.length == 0 ? (
        <div className={styles.customMessage}>
          <h1>No records found</h1>
        </div>
      ) : (
        v.map(createCard)
      )}

      {/* Pagination --> Show the Pagination if data exists,
       and enable the traversal only if the data is more than 10, and show 10 data per page in the UI.*/}

      {x.length == 0 ? null : (
        <Container>
          <Card className={styles.paginateCard}>
            <Card.Body>
              <ReactPaginate
                previousLabel={"<<"}
                nextLabel={">>"}
                pageCount={pageCount}
                onPageChange={pageChange}
                containerClassName={styles.paginationButtons}
                previousLinkClassName={"previousButton"}
                nextLinkClassName={"nextButton"}
                disabledClassName={styles.paginationDisabled}
                activeClassName={styles.paginationActive}
              ></ReactPaginate>
            </Card.Body>
          </Card>
        </Container>
      )}
    </Fragment>
  );
}

export default RenderContent;
