import os

cur_dir = os.path.dirname(os.path.abspath(__file__))                # config
src_dir = os.path.dirname(cur_dir)                                  # src
base_dir = os.path.dirname(src_dir)                                 # base
model_repo = 'ajupyter/EmoLLM_aiwei'

# model
model_dir = os.path.join(base_dir, 'model')                         # model
embedding_path = os.path.join(model_dir, 'embedding_model')         # embedding
rerank_path = os.path.join(model_dir, 'rerank_model')  	        	# embedding
llm_path = os.path.join(model_dir, 'pythia-14m')                    # llm

# data
data_dir = os.path.join(base_dir, 'data')                           # data
knowledge_json_path = os.path.join(data_dir, 'knowledge.json')      # json
knowledge_pkl_path = os.path.join(data_dir, 'knowledge.pkl')        # pkl
doc_dir = os.path.join(data_dir, 'txt')   
qa_dir = os.path.join(data_dir, 'json')   

# log
log_dir = os.path.join(base_dir, 'log')                             # log
log_path = os.path.join(log_dir, 'log.log')                         # file

# vector DB
vector_db_dir = os.path.join(data_dir, 'vector_db')

# RAG related
# select num: 代表rerank 之后选取多少个 documents 进入 LLM
# retrieval num： 代表从 vector db 中检索多少 documents。（retrieval num 应该大于等于 select num）
select_num = 3
retrieval_num = 10

# LLM key
glm_key = ''

# prompt
prompt_template = """
	{system_prompt}
	根据下面检索回来的信息，回答问题。
	{content}
	问题：{query}
"""