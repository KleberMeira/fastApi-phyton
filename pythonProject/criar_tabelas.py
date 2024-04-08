from core.configs import settings
from core.database import engine

async def create_table() -> None:
    import models.__all_models
    print('Criando tabela no banco de dados...')

    async with engine.begin() as conn:
        await conn.run_async(settings.DBbaseModel.metadata.drop_all)
        await conn.run_async(settings.DBbaseModel.metadata.create_all)
    print('Tabelas criadas...')

if __name__ == '__main__':
    import asyncio
    asyncio.run(create_table())
