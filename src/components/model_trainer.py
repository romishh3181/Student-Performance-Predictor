import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    RandomForestRegressor,
    GradientBoostingRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
class ModelTrainer:
    def __init__(self):
        self.model_trainer_path=ModelTrainerConfig() 
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting train and test input data")
            X_train,Y_train,X_test,Y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regressor":KNeighborsRegressor(),
                "XGBRegressor":XGBRegressor(),
                "CBRegressor":CatBoostRegressor(),
                "AdaBoostRegressor":AdaBoostRegressor(),
                "GradientBoost":GradientBoostingRegressor(),

            }
            model_report:dict=evaluate_model(X_train=X_train,Y_train=Y_train,X_test=X_test,Y_test=Y_test,models=models)
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]
            if(best_model_score<0.6):
                raise CustomException("No best model found")
            logging.info("Best found model on both training and test dataset")
            save_object(file_path=self.model_trainer_path.trained_model_file_path,obj=best_model)
            predicted=best_model.predict(X_test)
            r2_scoring=r2_score(Y_test,predicted)
            return r2_scoring

        except Exception as e:
                raise CustomException(e,sys)
