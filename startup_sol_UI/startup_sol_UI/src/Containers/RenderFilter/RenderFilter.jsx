import React, { useContext, useEffect, useState } from "react";

import { FetchDataContext } from "../../Context/FetchDataContext";
import CheckBoxFilter from "../../Components/Checkbox/Checkbox";
import classes from "./RenderFilter.module.css";
import Button from "react-bootstrap/Button";
import { SearchFilterContext } from "../../Context/SearchFilterContext";

import { MdOutlineArrowDropDownCircle } from "react-icons/md";

function RenderFilter() {
  const { dataFromAPI, OnSubmit } = useContext(FetchDataContext);
  const { SearchOnAppliedFilter } = useContext(SearchFilterContext);

  const [isActive, setIsActive] = useState(false);
  const [isActiveName, setIsActiveName] = useState();

  const {
    setIsResetFilter,
    btnIsHighlighted,
    setBtnIsHighlighted,
    setMasterSelected,
    masterSelected,
    setIsCheckValue
  } = useContext(FetchDataContext);

  // Clear the filters applied by the user, and calls the API with the query and target.

  const clearFilter = () => {
    setMasterSelected([]);
    setIsCheckValue([]);
    setIsResetFilter(true);
    setTimeout(() => {
      setIsResetFilter(false);
    }, 1000);
    // setIsResetFilter(false);
    OnSubmit();
  };

  useEffect(() => {
    if (masterSelected.length === 0) {
      return;
    }
    setBtnIsHighlighted(true);

    const timer = setTimeout(() => {
      setBtnIsHighlighted(false);
    }, 300);

    return () => {
      clearTimeout(timer);
    };
  }, [masterSelected]);

  var filter = dataFromAPI["filters"];
  var filterList = [
    "Asset type",
    "Channel",
    "Area",
    "Collection",
    "Subject",
    "Technology"
  ];

  // Active function, it enables the user to open and close the respective filter box when clicked.
  const activate = event => {
    if (event.target.innerHTML === isActiveName || isActiveName == null) {
      setIsActiveName(event.target.innerHTML);
      setIsActive(() => !isActive);
    } else {
      setIsActive(false);
      setTimeout(() => {
        setIsActiveName(event.target.innerHTML);
        setIsActive(true);
      }, 100);
    }
  };

  const buttonClasses = `${classes.clearButton} ${
    btnIsHighlighted ? classes.bump : ""
  }`;

  console.log(masterSelected)
  return (
    <>
      <div className={classes.containerFilter}>
        {/* Check for the data from thr API and if the selected filter values(selected by user) are null,
         only show the Filter heading and Apply button. */}
        <div className={classes.filterHeading}>
          {masterSelected.length === 0 ? (
            <h3 className={classes.filterHeadingTitle}>
              Filter
              <br />
              {/* If the checkboxes in filter  are not checked show only apply button. */}
              {/* <Button
                variant="outline-success"
                className={classes.clearButton}
                type="button"
                onClick={SearchOnAppliedFilter}
              >
                Apply
              </Button> */}
            </h3>
          ) : (
            <h3 className={classes.filterHeadingTitle}>
              Filter
              <br />
              {/* If the checkboxes in filter are checked show reset and apply button. */}
              <Button
                variant="outline-danger"
                className={classes.clearButton}
                type="button"
                onClick={clearFilter}
              >
                Reset
              </Button>
              <Button
                variant="outline-success"
                className={buttonClasses}
                type="button"
                onClick={SearchOnAppliedFilter}
              >
                Apply
              </Button>
            </h3>
          )}

          {/* Map through the filter data from the API and hence create the filter checkboxes. */}
          {filter.map((e, i) => (
            <>
              {e.name === "date_of_publication" ? (
                <div className={classes.filterBox}>{/* {e.name} */}</div>
              ) : (
                <div className={classes.filterBox}>
                  <span>
                    <MdOutlineArrowDropDownCircle
                      className={classes.dropDownCircle}
                    />
                  </span>
                  {/* Call the onClick method when user clicks on title of the respective filters */}
                  <h3 className={classes.FilterTitle} onClick={activate}>
                    {e.ui_name}
                    {/* {filterList[i]} */}
                  </h3>

                  <hr className={classes.FilterTitleLine} />
                  <div className={classes.row}>
                    {/* Send the active status and filter-box header to Checkbox filter for opening the respective filter box on user click,
                     and also to manage the checked status */}
                    <CheckBoxFilter
                      name={e.name}
                      uiName = {e.ui_name}
                      active={isActive}
                      value={isActiveName}
                    />
                  </div>
                  {/* <hr /> */}
                  {/* <br /> */}
                </div>
              )}
            </>
          ))}
        </div>
      </div>
    </>
  );
}

export default RenderFilter;
