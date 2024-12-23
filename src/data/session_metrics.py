import pandas as pd


def get_session_metrics(df: pd.DataFrame, user_id: int) -> pd.DataFrame:
    """
    Given a pandas DataFrame in the format of the train dataset and a user_id, return the following metrics for every session_id of the user:
        - user_id (int) : the given user id.
        - session_id (int) : the session id.
        - total_session_time (float) : The time passed between the first and last interactions, in seconds. Rounded to the 2nd decimal.
        - cart_addition_ratio (float) : Percentage of the added products out of the total products interacted with. Rounded ot the 2nd decimal.

    If there's no data for the given user, return an empty Dataframe preserving the expected columns.
    The column order and types must be scrictly followed.

    Parameters
    ----------
    df : pandas DataFrame
       DataFrame  of the data to be used for the agent.
    user_id : int
        Id of the client.

    Returns
    -------
    Pandas Dataframe with some metrics for all the sessions of the given user.
    """
    
   # Filtrar el DataFrame por el user_id proporcionado
    user_df = df[df['user_id'] == user_id]

    if user_df.empty:
        # Si no hay datos para el user_id, devolver un DataFrame vacío con columnas esperadas
        return pd.DataFrame(columns=["user_id", "session_id", "total_session_time", "cart_addition_ratio"])

    # Asegurar que timestamp_local es datetime
    user_df = user_df.copy()  # Evitar SettingWithCopyWarning
    user_df['timestamp_local'] = pd.to_datetime(user_df['timestamp_local'])

    # Agrupar por session_id y calcular métricas
    session_metrics = user_df.groupby('session_id').apply(
        lambda group: pd.Series({
            'total_session_time': round((group['timestamp_local'].max() - group['timestamp_local'].min()).total_seconds(), 2),
            'cart_addition_ratio': round(group['add_to_cart'].sum() / len(group) * 100, 2)  # Porcentaje
        })
    ).reset_index()

    # Añadir columna user_id y ordenar las columnas como se requiere
    session_metrics['user_id'] = user_id
    session_metrics = session_metrics[['user_id', 'session_id', 'total_session_time', 'cart_addition_ratio']]

    return session_metrics