package java_function;

import java.util.*;
import java.util.stream.Collectors;
import tech.tablesaw.api.*;


public class SessionMetrics {
    public static Table getSessionMetrics(Table df, int userId) {
        /**
         * Given a Table (representing the data) and a user_id, return the following metrics for every session_id of the user:
         *     - user_id (int) : the given user id.
         *     - session_id (int) : the session id.
         *     - total_session_time (float) : The time passed between the first and last interactions, in seconds. Rounded to the 2nd decimal.
         *     - cart_addition_ratio (float) : Percentage of the added products out of the total products interacted with. Rounded to the 2nd decimal.
         *
         * Order the entries ascending by user_id and session_id. The column order and types must be strictly followed.
         *
         * Parameters
         * ----------
         * data : Table
         *     A Tablesaw Table where each row represents a record of data with columns:
         *     - "user_id" (Integer)
         *     - "session_id" (Integer)
         *     - "timestamp_local" (LocalDateTime or String in timestamp format)
         *     - "add_to_cart" (Integer, where 1 indicates True, and 0 indicates False)
         *
         * userId : int
         *     Id of the client.
         *
         * Returns
         * -------
         * Table
         *     A Tablesaw Table with the following columns:
         *     - "user_id" (Integer)
         *     - "session_id" (Integer)
         *     - "total_session_time" (Float rounded to 2 decimal places)
         *     - "cart_addition_ratio" (Float rounded to 2 decimal places)
         *
         * If no data exists for the given user, return an empty Table with the specified schema.
         */

    }
}