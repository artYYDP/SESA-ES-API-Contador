from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

DATABASE_URL = "sqlite:///contador.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()

class ClickCount(Base):
	__tablename__ = "click_counts"
	id = Column(Integer, primary_key=True)
	grupo = Column(String)
	painel = Column(String)
	data = Column(DateTime)
	quantidade = Column(Integer, default=1)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route('/api/contar', methods=['GET'])
def contar():
	grupo = request.args.get('grupo')
	painel = request.args.get('painel')
	if not grupo or not painel:
		return jsonify({'error': 'Faltando parâmetro'}), 400

	session = Session()
	fuso = ZoneInfo('America/Sao_Paulo')
	agora = datetime.datetime.now(fuso)
	click = ClickCount(grupo=grupo, painel=painel, data=agora, quantidade=1)
	session.add(click)
	session.commit()
	session.close()
	return jsonify({'success': True})

@app.route('/api/consulta', methods=['GET'])
def consulta():
	session = Session()
	result = session.query(ClickCount).all()
	resp = [
		{
			"id": c.id,
			"grupo": c.grupo,
			"painel": c.painel,
			"quantidade": c.quantidade,
			"data": c.data.strftime('%Y-%m-%d %H:%M:%S')
		} for c in result
	]
	session.close()
	return jsonify(resp)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)