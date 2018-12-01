pragma solidity 0.5.0;


contract WorldSkills {

    struct  Estate {
    uint estate_id;
    address owner;
    string info;
    uint squere;
    uint useful_squere;
    bool present_status;
    bool sale_status;
    bool pledge_status;
    }
    
    struct Present {
        uint estate_id;
        address address_from;
        address address_to;
        uint deadline;
    }
    
    struct Sale {
        uint estate_id;
        address owner;
        uint price;
        uint time;
        uint deadline;
        address payable[] customers;
        uint[] prices;
    }
    
    struct Pledge {
        uint estate_id;
        address payable owner_address;
        address payable money_address;
        uint money;
        uint time;
        uint deadline;
        bool p_status;
    }
    
    Estate[] estates;
    Present[] presents;
    Sale[] sales;
    Pledge[] pledges;
    
    address admin = 0xAc771378BB6c2b8878fbF75F80880cbdDefd1B1e;
    //address admin = 0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c;
    address payable default_address = 0x0000000000000000000000000000000000000000;

    // РАБОТАЕТ
    function get_estates_number() public view returns(uint) {
        return estates.length;
    }
    
    function get_presents_number() public view returns(uint) {
        return presents.length;
    }
    
    function get_sales_number() public view returns(uint) {
        return sales.length;
    }
    
    function get_pledges_number() public view returns(uint) {
        return pledges.length;
    }
    
    
    
    // РАБОТАЕТ
    function get_estates(uint estate_number) public view returns(uint, address, string memory, uint, uint) {
        return(estates[estate_number].estate_id, estates[estate_number].owner, estates[estate_number].info, estates[estate_number].squere, estates[estate_number].useful_squere);
    }
    // РАБОТАЕТ
    function get_estates_statuses(uint estate_number) public view returns(bool, bool, bool) {
        return(estates[estate_number].present_status, estates[estate_number].sale_status, estates[estate_number].pledge_status);
    }
    
    function get_presents(uint present_number) public view returns(uint, address, address, uint) {
        return(presents[present_number].estate_id, presents[present_number].address_from, presents[present_number].address_to, presents[present_number].deadline);
    }
    
    function get_sales(uint sale_number) public view returns(uint, address, uint, uint, uint, address payable[] memory, uint[] memory prices) {
        return(sales[sale_number].estate_id, sales[sale_number].owner, sales[sale_number].price, sales[sale_number].time, sales[sale_number].deadline, sales[sale_number].customers, sales[sale_number].prices);
    }
    
    function get_pledges(uint pledge_number) public view returns(uint, address, address, uint, uint, uint, bool) {
        return(pledges[pledge_number].estate_id, pledges[pledge_number].owner_address, pledges[pledge_number].money_address, pledges[pledge_number].money, pledges[pledge_number].time, pledges[pledge_number].deadline, pledges[pledge_number].p_status);
    }
    
    
    
            //Admin's function
    // РАБОТАЕТ
    //Создать объект собственности
    function create_estate(address owner, string memory info, uint squere, uint useful_squere) public {
        require(msg.sender == admin);
        estates.push(Estate(estates.length, owner, info, squere, useful_squere, false, false, false));
    }
    
    // ТЕСТ Создать объект собственности
    /* function test_create_estate(address owner, string memory info, uint useful_squere) public {
        require(msg.sender == admin);
        for(uint i=0; i < 5; i++) {
            estates.push(Estate(estates.length, owner, info, 10*i, useful_squere, false, false, false));
        }
		
    }
	*/
    

            
            //Present's functions
            
    // Создать предложение подарка
    function create_present(uint estate_id, address address_to, uint deadline) public {
        require(msg.sender == estates[estate_id].owner);
        require(estates[estate_id].present_status == false);
        require(estates[estate_id].sale_status == false);
        require(estates[estate_id].pledge_status == false);
        presents.push(Present(estate_id, msg.sender, address_to, now + deadline));
        estates[estate_id].present_status = true;
    } 
    
    // Отменить свой подарок(доступна до принятие подарка адресатом)
    function cancel_present(uint present_number) payable public {
        require(msg.sender == presents[present_number].address_from);
        estates[presents[present_number].estate_id].present_status = false;
        delete presents[present_number];
        
    }
    
    // Принять подарок
    function confirm_present(uint present_number) payable public {
        require(msg.sender == presents[present_number].address_to);
        require(presents[present_number].deadline <= now);
        estates[presents[present_number].estate_id].owner = presents[present_number].address_to;
        estates[presents[present_number].estate_id].present_status = false;
        delete presents[present_number];
        
    }
    
    // Удалить подарок, т.к. срок истек
    function present_time_out(uint present_number) public {
        require(presents[present_number].deadline < now);
        require(msg.sender == admin);
        cancel_present(present_number);
    }
    
    
    
            //Sale's functions
    
    // Разместить объявление о продаже
    function create_sale(uint estate_id, uint price, uint date) public {
       require(msg.sender == estates[estate_id].owner);
       require(estates[estate_id].present_status == false);
       require(estates[estate_id].sale_status == false);
       require(estates[estate_id].pledge_status == false);
       address payable[] memory customers;
       uint[] memory prices;
       sales.push(Sale(estate_id, msg.sender, price, date, date + now, customers, prices));
       estates[estate_id].sale_status = true;
    }
    
    // Отменить объявление о продаже и вернуть деньги всем, кто успел внести
    function cancel_sale(uint sale_number) public  {
        require(msg.sender == sales[sale_number].owner);
        for (uint i = 0; i < sales[sale_number].customers.length; i++){
            (sales[sale_number].customers[i]).transfer(sales[sale_number].prices[i]);
        }
        estates[sales[sale_number].estate_id].sale_status = false;
        delete sales[sale_number];
        
    }
    
    // Выбрать чтобы купить
    function check_to_buy(uint sale_number) public payable {
        require(msg.sender != sales[sale_number].owner);
        require(msg.value >= sales[sale_number].price);
        uint status = 0;
        for (uint i=0; i < sales[sale_number].customers.length; i++) {
            if (sales[sale_number].customers[i] == msg.sender) {
                status = 1;
                break;
            }
        }
        require(status == 0);
        sales[sale_number].customers.push(msg.sender);
        sales[sale_number].prices.push(msg.value);
    }
    
    // Отменить выбор покупки
    function cancel_to_buy(uint sale_number) public payable {
        for (uint i=0; i<sales[sale_number].customers.length; i++){
            if (sales[sale_number].customers[i] == msg.sender){
                msg.sender.transfer(sales[sale_number].prices[i]);
                delete sales[sale_number].customers[i];
                delete sales[sale_number].prices[i];
            }
        }
    }
    
    // Подтвердить продажу и вернуть деньги остальным
    function confirm_sale(uint sale_number, uint sale_to) public payable {
        require(msg.sender == sales[sale_number].owner);
        estates[sales[sale_number].estate_id].owner = sales[sale_number].customers[sale_to];
        msg.sender.transfer(sales[sale_number].prices[sale_to]);
        for (uint i=0; i<sales[sale_number].customers.length; i++){
            if (i != sale_to) {
                sales[sale_number].customers[i].transfer(sales[sale_number].prices[i]);
            }
        }
        estates[sales[sale_number].estate_id].sale_status = false;
        delete sales[sale_number];
    }

    // Удалить продажу, т.к. время истекло 
    function sale_time_out(uint sale_number) public {
        require(sales[sale_number].deadline < now);
        require(msg.sender == admin);
        cancel_sale(sale_number);
    }
    
    
    
            // Pledge's function
    
    //Создать объявление о залоге
    function create_pledge(uint estate_id, uint money, uint time) public {
        require(msg.sender == estates[estate_id].owner);
        require(estates[estate_id].present_status == false);
        require(estates[estate_id].sale_status == false);
        require(estates[estate_id].pledge_status == false);
        uint deadline = 0;
        address payable money_address = default_address;
        pledges.push(Pledge(estate_id, msg.sender, money_address, money, time, deadline, false));
        estates[estate_id].pledge_status = true;
    }
    
    // Отменить свое предложение о залоге и вернуть деньги залогодавателю
    function cancel_pledge(uint pledge_number) public payable {
        require(msg.sender == pledges[pledge_number].owner_address);
        if (pledges[pledge_number].money_address != default_address) {
            pledges[pledge_number].money_address.transfer(pledges[pledge_number].money);
        }
        estates[pledges[pledge_number].estate_id].pledge_status = false;
        delete pledges[pledge_number];
        
    }
    
    // Выбрать чтобы выдать залог
    function check_to_pledge(uint pledge_number) public payable {
        require(msg.value == pledges[pledge_number].money);
        require(msg.sender != pledges[pledge_number].owner_address);
        pledges[pledge_number].money_address = msg.sender;
    }
    
    // Отменить предложенный залог
    function cancel_to_pledge(uint pledge_number) public payable {
        require(msg.sender == pledges[pledge_number].money_address);
        msg.sender.transfer(pledges[pledge_number].money);
        pledges[pledge_number].money_address = default_address;
    }
    
    // Принять деньги в залог, начинается отсчет времени
    function confirm_pledge(uint pledge_number) public {
        require(msg.sender == pledges[pledge_number].owner_address);
        pledges[pledge_number].deadline = pledges[pledge_number].time + now;
        pledges[pledge_number].owner_address.transfer(pledges[pledge_number].money);
    }
  
    //Отказаться от предложения
    function refuse_pledge(uint pledge_number) payable public {
        require(msg.sender == pledges[pledge_number].owner_address);
        pledges[pledge_number].money_address.transfer(pledges[pledge_number].money);
        pledges[pledge_number].money_address = default_address;
    }
    
    // Вернуть деньги, полученные в залог
    function finish_pledge(uint pledge_number) payable public {
        require(msg.value == pledges[pledge_number].money);
        require(msg.sender == pledges[pledge_number].owner_address);
        require(pledges[pledge_number].deadline <= now);
        pledges[pledge_number].money_address.transfer(pledges[pledge_number].money);
        estates[pledges[pledge_number].estate_id].pledge_status = false;
        delete pledges[pledge_number];
    }
    
    // Завершить залог по истечению времени
    function pledge_time_out(uint pledge_number) payable public {
        require(pledges[pledge_number].deadline < now);
        require(msg.sender == admin);
        estates[pledges[pledge_number].estate_id].owner = pledges[pledge_number].money_address;
        estates[pledges[pledge_number].estate_id].pledge_status = false;
        delete pledges[pledge_number];
    }
    
}

