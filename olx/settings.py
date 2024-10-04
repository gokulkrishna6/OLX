<!-- create by athul -->

{% extends 'company/src/html/base.html' %}

{% block content %}
{% load static %}


<style>
  .calendar-title {
    font-size: 18px;
    margin-bottom: 10px;
    color: #333;
  }

  .calendar {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    width: 300px;
    position: absolute;

    left: 51% !important;
    z-index: 1;
    display: none;
  }

  .header {
    background-color: #3498db;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }

  #prevBtn,
  #nextBtn {
    background: none;
    border: none;
    color: white;
    cursor: pointer;
    font-size: 16px;
  }

  #monthYear {
    font-size: 18px;
    font-weight: bold;
  }

  .days {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 5px;
    padding: 10px;
  }

  .day {
    padding: 10px;
    text-align: center;
    border-radius: 5px;
    cursor: pointer;
  }

  .day.current {
    background-color: #3498db;
    color: white;
  }

  .day.selected {
    background-color: #2ecc71;
    color: white;
  }

  .input-container {
    position: relative;

  }


  .label-inside {
    position: absolute;
    top: 50%;
    left: 30px;

    transform: translateY(-50%);
    pointer-events: none;
    background-color: white;
    transition: all 0.3s ease;

  }

  .form-control:focus+.label-inside,
  .form-control:not(:placeholder-shown)+.label-inside {
    top: 0;
    font-size: 12px;


  }
</style>

<div class="body-wrapper">
  <div class="container-fluid">
    <!--  Row 1 -->
    <div class="row mb-5 mt-3">
      <div class="col-md-3"></div>
      <div class="col-md-5">

        <a href="" id="b1" class="btn  text-white"
          style="margin-right: 10px; background-color: rgb(252, 3, 3,0.7);border-radius: 20px;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">Add
          Sale <i class="fa fa-plus"></i></a>
        <a href="" id="b2" class="btn  text-white"
          style="margin-right: 10px;background-color: rgba(3, 161, 252, 0.7);border-radius: 20px;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">Add
          Purchase <i class="fa fa-plus"></i></a>
        <a href="" id="b3" class="btn text-primary mt-1"
          style="border-radius: 20px;border: 1px solid rgb(40, 12, 222);background-color: white;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">Add
          More <i class="fa fa-plus"></i></a>

      </div>

    </div>
    <div class="row">
      <div class="col-lg-12 d-flex align-items-strech">
        <div class="mx-auto w-75" style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
          <form action="" method="post">
            {% csrf_token %}
            <div>
              <div class="mx-4">
                <br>
                <h6>Edit Loan Account</h6>
                <br>
              </div>
          
              <div class="row mx-2 mb-4">
                
                <!-- <div class="col">
                  <input type="text" name="account_name" value="{{data.account_name}}" class="form-control" placeholder="Account Name *" aria-label="Account Name" required>
                </div> -->
                <div class="col">
                  <select name="party" id="party" class="form-select">
                    {% for party_option in parties %}
                        <option value="{{ party_option.id }}" {% if party_option.id == data.party.id %}selected{% endif %}>
                            {{ party_option.party_name }}
                        </option>
                    {% endfor %}
                </select>
                
                </div>
                <div class="col">
                  <input type="text" value="{{data.lender_bank}}" name="lender_bank" class="form-control" placeholder="Lender Bank" aria-label="Lender Bank" required>
                </div>
              </div>

              <div class="row mx-2 mb-4">
                <div class="col">
                  <input type="number" value="{{data.account_number}}" name="account_number" class="form-control" placeholder="Account Number" aria-label="Account Number"
                    required>
                </div>
                <div class="col">
                  <input type="text" value="{{data.description}}" name="description" class="form-control" placeholder="Description" aria-label="Description" required>

                </div>
                
              </div>
              <hr class="mx-3">

              <div class="row mx-2 mb-4">
                <div class="col">
                  <input type="number" value="{{data.balance_amount}}" name="current_balance" class="form-control" placeholder="Current balance *"
                    aria-label="Current balance *">
                </div>


                <div class="col">
                  <div class="calendar-box">
                    <input value="{{data.date}}" name="date" type="text" class="form-control" id="dateInput" value="{{data.date}}">
                    <div class="calendar" id="calendar">
                      <div class="header">
                        <button id="prevBtn">&lt;</button>
                        <h2 id="monthYear">Month Year</h2>
                        <button id="nextBtn">&gt;</button>
                      </div>
                      <div class="days" id="daysContainer"></div>
                    </div>
                  </div>


                </div>

              </div>

              <div class="row mx-2 mb-4 ">
                <div class="col">
                  <select name="loan_received" class="form-select" aria-label="Default select example" id="change">
                    {% if data.loan_received == "Cash" %}
                        <option value="Cash" selected>Cash</option>
                        <option value="this">ADD NEW BANK ACCOUNT?</option>
                    {% elif data.loan_received == "this" %}
                        <option value="{{ data.loan_received }}" selected>ADD NEW BANK ACCOUNT?</option>
                        <option value="Cash">Cash</option>
                    {% else %}
                        <option value="{{ data.loan_received }}" selected>{{ data.loan_received }}</option>
                        <option value="Cash">Cash</option>
                        <option value="this">ADD NEW BANK ACCOUNT?</option>
                    {% endif %}
                </select>





                </div>
                <div class="col">

                </div>


              </div>

              <div class="row mx-2 mb-4">
                <div class="col">
                  <div class="input-group ">
                    <input name="rate" type="text" value="{{data.interest_rate}}" class="form-control" placeholder="Interest Rate" aria-label="Interest Rate"
                      aria-describedby="basic-addon2">
                    <span class="input-group-text bg-light " id="basic-addon2">% per annum</span>
                  </div>
                </div>


                <div class="col">
                  <input name="duration" value="{{data.duration}} " type="text" class="form-control" placeholder="Term Duration (In Months)"
                    aria-label="Term Duration (In Months)" required>

                </div>

              </div>

              <div class="row mx-2 mb-4">

                <div class="input-container col">
                  <input name="fee" value="{{data.proccessing_fee}}" type="text" class="form-control" placeholder=" " aria-label="Processing Fee">
                  <label class="label-inside">Processing Fee</label>
                </div>

                <div class="col">
                  <select name="lr" class="form-select" aria-label="Default select example" id="change">
                    {% if data.lr == "Cash" %}
                        <option value="Cash" selected>Cash</option>
                        <option value="this">ADD NEW BANK ACCOUNT?</option>
                    {% elif data.lr == "this" %}
                        <option value="{{ data.lr }}" selected>ADD NEW BANK ACCOUNT?</option>
                        <option value="Cash">Cash</option>
                    {% else %}
                        <option value="{{ data.lr }}" selected>{{ data.lr }}</option>
                        <option value="Cash">Cash</option>
                        <option value="this">ADD NEW BANK ACCOUNT?</option>
                    {% endif %}
                </select>
                </div>



              </div>
              <div class="row me-4 mb-4">

       

           
             
                <div class="modal-footer">
           
                  <button type="submit" class="btn btn-primary">Save changes</button>
                </div>

              </div>

             
            </div>
          </form>
        </div>
      </div>

    </div>
  









  </div>
</div>



<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel"> ADD BANK ACCOUNT
        </h5>

        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <hr>
      <div class="modal-body">
        <div class="row mx-2 mb-4">
          <div class="col">
            <input type="text" class="form-control" placeholder="First name" aria-label="First name">
          </div>
          <div class="col">
            <input type="text" class="form-control" placeholder="Last name" aria-label="Last name">
          </div>

          <div class="col">
            <input type="text" class="form-control" placeholder="First name" aria-label="First name">
          </div>
        </div>

        <div class="row mx-2 mb-4">
          <div class="col">
            <input type="checkbox" id="checkbox_one" name="question1" data-trigger="hidden_fields_one" class="trigger">
            Print UPI QR code on invoices
          </div>


        </div>

        <div class="row mx-2 mb-4">
          <div class="col">
            <div id="hidden_fields_one" class="hidden row" class="mx-2 mb-4">
              <div class="col">
                <input type="text" id="hidden_one" name="hidden" placeholder="Account Number" class="form-control">
              </div>
              <div class="col">
                <input type="text" id="hidden_one" name="hidden" placeholder="Account Number" class="form-control">
              </div>
              <div class="col">
                <input type="text" id="hidden_one" name="hidden" placeholder="Account Number" class="form-control">
              </div>

            </div>
          </div>
        </div>




      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

<script>
  $('#change').change(function () {
    var selectedOption = $(this).val();

    if (selectedOption === "1") {

    } else if (selectedOption === "this") {

      $('.modal').modal('show');
    }
  });
</script>


<script>
  const daysContainer = document.getElementById("daysContainer");
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const monthYear = document.getElementById("monthYear");
  const dateInput = document.getElementById("dateInput");
  const calendar = document.getElementById("calendar");

  let currentDate = new Date();
  let selectedDate = null;

  function handleDayClick(day) {
    selectedDate = new Date(
      currentDate.getFullYear(),
      currentDate.getMonth(),
      day
    );


    const formattedDate = `${selectedDate.getDate().toString().padStart(2, '0')}/${(selectedDate.getMonth() + 1).toString().padStart(2, '0')}/${selectedDate.getFullYear()}`;

    dateInput.value = formattedDate;
    calendar.style.display = "none";
    renderCalendar();
  }

  function createDayElement(day) {
    const date = new Date(currentDate.getFullYear(), currentDate.getMonth(), day);
    const dayElement = document.createElement("div");
    dayElement.classList.add("day");

    if (date.toDateString() === new Date().toDateString()) {
      dayElement.classList.add("current");
    }
    if (selectedDate && date.toDateString() === selectedDate.toDateString()) {
      dayElement.classList.add("selected");
    }

    dayElement.textContent = day;
    dayElement.addEventListener("click", () => {
      handleDayClick(day);
    });
    daysContainer.appendChild(dayElement);
  }

  function renderCalendar() {
    daysContainer.innerHTML = "";
    const firstDay = new Date(
      currentDate.getFullYear(),
      currentDate.getMonth(),
      1
    );
    const lastDay = new Date(
      currentDate.getFullYear(),
      currentDate.getMonth() + 1,
      0
    );

    monthYear.textContent = `${currentDate.toLocaleString("default", {
      month: "long"
    })} ${currentDate.getFullYear()}`;

    for (let day = 1; day <= lastDay.getDate(); day++) {
      createDayElement(day);
    }
  }

  prevBtn.addEventListener("click", () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar();
  });

  nextBtn.addEventListener("click", () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar();
  });

  dateInput.addEventListener("click", () => {
    calendar.style.display = "block";
    positionCalendar();
  });

  document.addEventListener("click", (event) => {
    if (!dateInput.contains(event.target) && !calendar.contains(event.target)) {
      calendar.style.display = "none";
    }
  });

  function positionCalendar() {
    const inputRect = dateInput.getBoundingClientRect();
    calendar.style.top = inputRect.bottom + "px";
    calendar.style.left = inputRect.left + "px";
  }

  window.addEventListener("resize", positionCalendar);

  renderCalendar();






  document.addEventListener("DOMContentLoaded", function () {

    const day = currentDate.getDate().toString().padStart(2, '0');
    const month = (currentDate.getMonth() + 1).toString().padStart(2, '0');
    const year = currentDate.getFullYear();

    const formattedDate = `${day}/${month}/${year}`;
    dateInput.value = formattedDate;
  });




  $(function () {

    $('.hidden').hide();

    $('.trigger').change(function () {


      var hiddenId = $(this).attr("data-trigger");

      if ($(this).is(':checked')) {

        $("#" + hiddenId).show();
      } else {
        $("#" + hiddenId).hide();
      }
    });
  });


var rawDate = $('#dateInput').val();
var formattedDate = moment(rawDate, 'DD-MM-YYYY').format('YYYY-MM-DD');

</script>

{% endblock %}