import httpx

class ApiService:
    BASE_URL = "http://127.0.0.1:8001"
    
    @staticmethod
    async def create_sale(data: dict):
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{ApiService.BASE_URL}/vendas/", json=data)
            response.raise_for_status()
            return response.json()
            
    @staticmethod
    async def get_sales_today():
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{ApiService.BASE_URL}/vendas/")
            response.raise_for_status()
            return response.json()
            
    @staticmethod
    async def delete_sale(sale_id: int):
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"{ApiService.BASE_URL}/vendas/{sale_id}")
            response.raise_for_status()
            return response.json()
            
    @staticmethod
    async def update_sale(sale_id: int, data: dict):
        async with httpx.AsyncClient() as client:
            response = await client.put(f"{ApiService.BASE_URL}/vendas/{sale_id}", json=data)
            response.raise_for_status()
            return response.json()
