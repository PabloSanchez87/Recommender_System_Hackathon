library(dplyr)

get_session_metrics <- function(df, user_id) {
  #' Get session metrics for a specific user
    #'
    #' Given a data frame in the format of the train dataset and a user_id, return the following metrics for every session_id of the user:
    #'     - user_id (integer): The given user id.
    #'     - session_id (integer): The session id.
    #'     - total_session_time (numeric): The time passed between the first and last interactions, in seconds. Rounded to the 2nd decimal.
    #'     - cart_addition_ratio (numeric): Percentage of the added products out of the total products interacted with. Rounded to the 2nd decimal.
    #'
    #' If there's no data for the given user, return an empty data frame preserving the expected columns.
    #' The column order and types must be strictly followed.
    #'
    #' @param df A data frame containing the session data, with the following columns:
    #'     - `user_id` (integer): The user ID.
    #'     - `session_id` (integer): The session ID.
    #'     - `timestamp_local` (POSIXct or character): The timestamp of the interaction.
    #'     - `add_to_cart` (integer): 1 if a product was added to the cart, 0 otherwise.
    #' @param user_id An integer representing the user ID for which metrics are calculated.
    #'
    #' @return A data frame with the following columns:
    #'     - `user_id` (integer)
    #'     - `session_id` (integer)
    #'     - `total_session_time` (numeric)
    #'     - `cart_addition_ratio` (numeric)
    #'
    #' If no data is found for the specified user ID, the function will return an empty data frame with the specified columns.
}