


class SendMessage{
    constructor(settings){
        



        this.settings=settings;
        this.form = document.querySelector(settings.form);
        this.formButton= document.querySelector(settings.button)
        console.log(this.formButton)
        if(this.form){
            this.url=this.form.getAttribute("action")
        }

        this.sendForm=this.sendForm.bind(this)
    }

    getFormObjects(){
        const formObjects={};

        const inputs = this.form.querySelectorAll("[name]");

        inputs.forEach(input => {
            formObjects[input.getAttribute("name")] = document.getElementById('messageInput').value;  
        });
        return formObjects;
    }

    onSubmission(event){
        event.preventDefault();
    }

    async sendForm(event){
        const mensagem = document.getElementById('messageInput').value
        try{
            this.onSubmission(event);
            innerMessageIn(document.getElementById('messageInput').value)
            const response = await fetch(this.url,{
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept:"application/json"
                },
                body: JSON.stringify({messageInput:mensagem})
            });
            let data = await response.json()
            innerMessageOut(data.output)
        }catch (error){
            throw new Error(error);
        }
        
    }

    init(){
        if(this.form){
            this.formButton.addEventListener("click", this.sendForm)
            return this;
        } 
    }
}

const sendMessage= new SendMessage({
    form: "[data-form]",
    button: "[data-button]",
});

const chat_mensagens = document.getElementById("mensagens");
const deleteButton = document.getElementById('clearChat')

async function  deleteMessages() {    
    let mensgaens = Array.from(chat_mensagens.children);
    console.log("delete")
    mensgaens.forEach(mensagem => {
        console.log(mensagem)
        console.log(mensagem.remove());
    });
    
    try{
        await fetch("/delete_messages",{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Accept:"application/json"
            },
            body: JSON.stringify({})
        });
    }catch (error){
        throw new Error(error);
    }
}

sendMessage.init()



function innerMessageIn(input){
    document.getElementById('messageInput').value=''
    mensagens = document.getElementById('mensagens')

    let human = document.createElement('p')
    human.classList.add('human')
    human.textContent = input

    mensagens.appendChild(human)
    mensagens.scrollTop = mensagens.scrollHeight
}
    

function innerMessageOut(output){
    mensagens = document.getElementById('mensagens')

    let ia = document.createElement('p')
    ia.classList.add('ia')
    ia.textContent = output

    mensagens.appendChild(ia)
    mensagens.scrollTop = mensagens.scrollHeight
}




