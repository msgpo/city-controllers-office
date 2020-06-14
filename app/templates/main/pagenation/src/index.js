import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import { Pagination } from "semantic-ui-react";

const INJECT_DIV_TAG = "result-list-target";
const container = document.getElementById(INJECT_DIV_TAG);

const ResultList = () => {
  const result_list = window.filtered_json;
  const page_size = 20;
  const totalPages = Math.round(result_list.length / page_size);
  const [page, setPage] = useState({ start: 0, end: page_size });

  function handlePageChange(data) {
    const activePage = data.activePage,
      start = (activePage - 1) * 20,
      end = activePage * 20;

    setPage({ start: start, end: end });
  }

  useEffect(() => {
    console.log("variable loaded!");
    console.log(result_list[0]);
  }, []);
  return (
    <>
      {result_list.slice(page.start, page.end).map((entry) => (
        <div key={entry.original_contract_id}>
          <div class="paper">
            <div class="ui grid">
              <div class="eight wide column">
                <h3 class="theme-primary">{entry.vendor}</h3>
                <p>
                  <i>ID: {entry.original_contract_id}</i>
                </p>
              </div>
              <div class="eight wide column">
                <div style={{ lineHeight: "20px" }}>
                  <div class="tag">TYPE</div>
                  <b>{entry.contract_structure_type}</b>
                </div>
                <div style={{ lineHeight: "20px" }}>
                  <div class="tag">DEPT</div>
                  <b>{entry.department_name}</b>
                </div>
              </div>
            </div>
          </div>
        </div>
      ))}
      <div style={{ marginTop: "50px", height: "30vh" }}>
        <Pagination
          defaultActivePage={1}
          totalPages={totalPages}
          onPageChange={(event, data) => handlePageChange(data)}
        />
      </div>
    </>
  );
};

class ResultListContainer extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return <ResultList />;
  }
}

ReactDOM.render(<ResultListContainer />, container);