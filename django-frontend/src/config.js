const BASE_URL ='http://localhost:8000/'


export const End = {
      'users' : BASE_URL+'users/'
}


 export const callApi = async (url ,method='GET' , data=null) => {
    try {
        if(method==='GET'){
            const response = await fetch(url, {
                method: method,
                headers: {
                    'Content-Type': 'application/json',
                },
            });
        }
        else{
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
    }

    const response = await fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
    });
        if (response.ok) {
             return await response.json();     
        } 
      
        
        else {
            console.error('Failed to add employee');
        }
    } catch (error) {
        console.error('Error adding employee:', error);
    }
        };