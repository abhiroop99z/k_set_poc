import React, { useContext } from "react";
import DatePicker, {registerLocale} from "react-datepicker";
import es from "date-fns/locale/es";

import "react-datepicker/dist/react-datepicker.css";
import "./DateFilter.css";
import { FetchDataContext } from "../../Context/FetchDataContext";

function DateFilter(props) {
  const {
    startDate,
    setStartDate,
    endDate,
    setEndDate
  } = useContext(FetchDataContext);

  registerLocale("es", es);

  // const [startDate, setStartDate] = useState();
  // const [endDate, setEndDate] = useState(null);

  const onChange = dates => {
    const [start, end] = dates;
    // setTargetedDate([start, end])
    setStartDate(start);
    setEndDate(end);
    // setTargetedDate([dates]);
  };
  // console.log(moment(endDate).format("DD-MM-YYYY"))
  

  return (
    <div>
      <DatePicker
        selected={startDate}
        onChange={onChange}
        startDate={startDate}
        endDate={endDate}
        month
        selectsRange
        isClearable
        showYearDropdown
        scrollableMonthYearDropdown
        locale="es"
        placeholderText = "Enter the date"
        disabled
      />
    </div>
  );
}

export default DateFilter;
